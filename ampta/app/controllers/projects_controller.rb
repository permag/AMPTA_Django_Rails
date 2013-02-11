class ProjectsController < ApplicationController
  before_filter :confirm_user, :only => [:edit, :update, :destroy]
  before_filter :sidenav

  def index
    @projects = Project.all # order...: Project.order("id DESC").all
  end

  def show
    @project = Project.find(params[:id])
    @project_owner = User.find(@project.owner_id)

    # is owner?
    if @project.owner_id == session[:user_id]
      @owner_menu = true
    end

    # belongs to project?
    if @project.users.exists?(session[:user_id])
      @belongs_menu = true
    end
  end

  def new
    @project = Project.new
    @users = get_users_except_current
  end

  def create
    @users = get_users_except_current
    @project = Project.new(params[:project])
    @project.owner_id = session[:user_id]


    respond_to do |format|
      if @project.save
        u = User.find(session[:user_id])
        u.projects << @project

        if params[:project][:project_users]
          params[:project][:project_users].each do |id| 
            @project.users << User.find(id)
          end
        end
        format.html { redirect_to project_path(@project), :notice => "Project was created." }
      else
        format.html { render :action => "new" }
      end
    end
  end

  def edit
    @project = Project.find(params[:id])
    @users = get_users_except_current
  end

  def update
    @users = get_users_except_current
    @project = Project.find(params[:id])

    respond_to do |format|
      if @project.update_attributes(params[:project])
        # clear join table
        @project.users.clear
        # current user
        u = User.find(session[:user_id])
        u.projects << @project
        if params[:project][:project_users]
          # add users to join table
          params[:project][:project_users].each do |id| 
            @project.users << User.find(id)
          end
        end
        format.html { redirect_to project_path(@project), :notice => "Project was updated." }
      else
        format.html { render :action => "edit" }
      end
    end
  end

  def destroy
    @project = Project.find(params[:id])
    @project.destroy

    respond_to do |format|
      format.html { redirect_to home_index_path, :notice => 'Project was deleted.' }
    end
  end

  def get_users_except_current
    current_user = User.find(session[:user_id])
    @users = (current_user.blank? ? User.all : User.find(:all, :conditions => ["id != ?", current_user.id]))
  end

  ##
  # check to see if user is project owner
  #
  def confirm_user
    unless Project.find(params[:id]).owner_id == session[:user_id]
      flash[:notice] = "You don't have the permission to do that."
      redirect_to home_index_path
      return false
    else
      return true
    end
  end

end
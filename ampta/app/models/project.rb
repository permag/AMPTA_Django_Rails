class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :project_users
  has_and_belongs_to_many :users
  has_many :tickets, :dependent => :destroy

  validates :name,
            :presence => true,
            :uniqueness => true,
            :length => { :in => 3..20, :allow_blank => true }
         
  validates_presence_of :description, :start_date, :end_date
  
  def project_users=(project_users)
    # empty. defines attribute :project_users for join table
  end

end

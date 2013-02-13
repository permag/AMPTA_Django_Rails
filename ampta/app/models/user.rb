class User < ActiveRecord::Base
  attr_accessible :first_name, :last_name, :email, :password
  has_and_belongs_to_many :projects
  has_many :tickets

  ##### has_secure_password
  attr_accessor :password
  before_save :create_hashed_password
  after_save :clear_password

  validates_presence_of :password

  validates :first_name,
            :presence => true,
            :length => { :in => 2..20, :allow_blank => true }

  validates :last_name,
            :presence => true,
            :length => { :in => 2..20, :allow_blank => true }

  validates :email,
            :presence => true,
            :uniqueness => true

  validates_format_of :email, 
                      :with => /^(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i

  
  # def self.authenticate(email, password)
  #   find_by_email(email).try(:authenticate, password)
  # end


  def create_hashed_password
    unless password.blank?
      self.salt = User.make_salt(email) if salt.blank?
      self.hashed_password = User.hash_password_with_salt(password, salt)
    end
  end

  def clear_password
    self.password = nil
  end


  def self.make_salt(email = "")
    Digest::SHA2.hexdigest("salt#{email}salt#{Time.now}salt")
  end

  def self.hash_password_with_salt(password = "", salt = "")
    Digest::SHA2.hexdigest("salt the #{password} with the #{salt}")
  end


  def self.authenticate(email_to_try = "", password_to_try = "")
    user = User.where("email = ?", email_to_try).first
    if user && user.password_match?(password_to_try, user.hashed_password)
      return user
    else
      return false
    end
  end

  def password_match?(password_to_check = "", hashed_password = "")
    hashed_password == User.hash_password_with_salt(password_to_check, salt)
  end

end
